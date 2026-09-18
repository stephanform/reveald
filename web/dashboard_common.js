// Shared chrome for the transposition-status dashboards: slicers, company
// spotlight search, tooltip, and the aggregation helpers every page needs to
// recompute its charts against whatever slice is currently active.
const DashboardCommon = (function(){
  const STATUS_LABEL_CLASS = { 'Transposed':'transposed', 'Not transposed':'pending', 'Not applicable':'na' };
  const D = TRANSPOSITION_DATA;
  const COMPANIES = D.companies;
  const STATUS_ORDER = D.statusOrder;

  function uniqueSorted(rows, key){
    return Array.from(new Set(rows.map(r => r[key]).filter(Boolean))).sort((a,b) => a.localeCompare(b));
  }

  function fmtPct(n, total){ return total ? (n/total*100).toFixed(1) + '%' : '0.0%'; }

  // ---------- tooltip ----------
  let tooltipEl = null;
  function ensureTooltip(){
    if (!tooltipEl){
      tooltipEl = document.getElementById('tooltip');
      if (!tooltipEl){
        tooltipEl = document.createElement('div');
        tooltipEl.id = 'tooltip';
        document.body.appendChild(tooltipEl);
      }
    }
    return tooltipEl;
  }
  function showTip(evt, html){
    const t = ensureTooltip();
    t.innerHTML = html;
    t.style.left = evt.clientX + 'px';
    t.style.top = evt.clientY + 'px';
    t.style.opacity = 1;
  }
  function hideTip(){ if (tooltipEl) tooltipEl.style.opacity = 0; }

  // ---------- aggregation ----------
  function frequency(rows, key){
    const counts = {};
    rows.forEach(r => { const v = r[key]; if (v) counts[v] = (counts[v]||0) + 1; });
    return Object.entries(counts).map(([name,count]) => ({name, count})).sort((a,b) => b.count - a.count);
  }

  function statusFrequency(rows, statusKey){
    const counts = {};
    STATUS_ORDER.forEach(s => counts[s] = 0);
    rows.forEach(r => { const v = r[statusKey]; if (v) counts[v] = (counts[v]||0) + 1; });
    return counts;
  }

  function crossTab(rows, groupKey, statusKey){
    const groups = {};
    rows.forEach(r => {
      const g = r[groupKey];
      if (!g) return;
      if (!groups[g]) groups[g] = { name:g, total:0, counts:{} };
      groups[g].total++;
      const s = r[statusKey];
      groups[g].counts[s] = (groups[g].counts[s]||0) + 1;
    });
    return Object.values(groups).sort((a,b) => b.total - a.total);
  }

  function mode(rows, key){
    const freq = frequency(rows, key);
    if (!freq.length) return { value:null, count:0, total:rows.length };
    return { value:freq[0].name, count:freq[0].count, total:rows.length };
  }

  // ---------- filtering ----------
  function currentFilters(){
    return {
      country: byId('countrySlicer') ? byId('countrySlicer').value : '',
      industry: byId('industrySlicer') ? byId('industrySlicer').value : '',
      nfrd: byId('nfrdSlicer') ? byId('nfrdSlicer').value : '',
      csrd: byId('csrdSlicer') ? byId('csrdSlicer').value : '',
    };
  }
  function byId(id){ return document.getElementById(id); }

  function applyFilters(rows, filters){
    return rows.filter(r =>
      (!filters.country || r.c === filters.country) &&
      (!filters.industry || r.i === filters.industry) &&
      (!filters.nfrd || r.nfrd === filters.nfrd) &&
      (!filters.csrd || r.csrd === filters.csrd)
    );
  }

  function dispatchFilterChange(){
    const filters = currentFilters();
    const rows = applyFilters(COMPANIES, filters);
    document.dispatchEvent(new CustomEvent('filterchange', { detail: { rows, filters, all: COMPANIES } }));
    const countEl = byId('slicerCount');
    if (countEl){ countEl.innerHTML = '<b>' + rows.length.toLocaleString() + '</b> / ' + COMPANIES.length.toLocaleString() + ' companies match'; }
  }

  function setupSlicers(){
    const countrySel = byId('countrySlicer');
    const industrySel = byId('industrySlicer');
    const nfrdSel = byId('nfrdSlicer');
    const csrdSel = byId('csrdSlicer');
    const resetBtn = byId('resetSlicers');

    function fill(sel, values, allLabel){
      if (!sel) return;
      sel.innerHTML = '';
      const allOpt = document.createElement('option');
      allOpt.value = ''; allOpt.textContent = allLabel;
      sel.appendChild(allOpt);
      values.forEach(v => {
        const opt = document.createElement('option');
        opt.value = v; opt.textContent = v;
        sel.appendChild(opt);
      });
    }
    fill(countrySel, uniqueSorted(COMPANIES, 'c'), 'All countries');
    fill(industrySel, uniqueSorted(COMPANIES, 'i'), 'All industries');
    fill(nfrdSel, STATUS_ORDER, 'All NFRD statuses');
    fill(csrdSel, STATUS_ORDER, 'All CSRD statuses');

    [countrySel, industrySel, nfrdSel, csrdSel].forEach(sel => {
      if (!sel) return;
      sel.addEventListener('change', () => {
        sel.classList.toggle('active', !!sel.value);
        dispatchFilterChange();
      });
    });
    if (resetBtn){
      resetBtn.addEventListener('click', () => {
        [countrySel, industrySel, nfrdSel, csrdSel].forEach(sel => { if (sel){ sel.value=''; sel.classList.remove('active'); } });
        dispatchFilterChange();
      });
    }
    dispatchFilterChange();
  }

  // ---------- company spotlight (highlight, never a hard filter) ----------
  function setupCompanySearch(){
    const input = byId('companySearch');
    const list = byId('companySuggest');
    const spotlight = byId('spotlight');
    if (!input || !list) return;

    let active = -1;
    let matches = [];

    function render(){
      const q = input.value.trim().toLowerCase();
      list.innerHTML = '';
      active = -1;
      if (!q){ list.classList.remove('open'); return; }
      matches = COMPANIES.filter(c => c.n.toLowerCase().includes(q)).slice(0, 30);
      if (!matches.length){
        const empty = document.createElement('div');
        empty.className = 'suggest-empty';
        empty.textContent = 'no match';
        list.appendChild(empty);
      } else {
        matches.forEach((c) => {
          const item = document.createElement('div');
          item.className = 'suggest-item';
          item.textContent = c.n + ' · ' + c.c;
          item.addEventListener('click', () => selectCompany(c));
          list.appendChild(item);
        });
      }
      list.classList.add('open');
    }

    function selectCompany(c){
      input.value = c.n;
      list.classList.remove('open');
      if (spotlight){
        spotlight.classList.add('show');
        spotlight.innerHTML =
          '<span class="co">' + escapeHtml(c.n) + '</span>' +
          '<span>country: <b>' + escapeHtml(c.c) + '</b></span>' +
          '<span>industry: <b>' + escapeHtml(c.i) + '</b></span>' +
          '<span>NFRD: <b>' + escapeHtml(c.nfrd) + '</b></span>' +
          '<span>CSRD: <b>' + escapeHtml(c.csrd) + '</b></span>' +
          '<span class="close" id="spotlightClose">reset ×</span>';
        document.getElementById('spotlightClose').addEventListener('click', clearSpotlight);
      }
      document.dispatchEvent(new CustomEvent('spotlightchange', { detail: { company: c } }));
    }

    function clearSpotlight(){
      input.value = '';
      if (spotlight){ spotlight.classList.remove('show'); spotlight.innerHTML=''; }
      document.dispatchEvent(new CustomEvent('spotlightchange', { detail: { company: null } }));
    }

    function escapeHtml(s){
      const d = document.createElement('div');
      d.textContent = s;
      return d.innerHTML;
    }

    input.addEventListener('input', render);
    input.addEventListener('keydown', (e) => {
      const items = Array.from(list.querySelectorAll('.suggest-item'));
      if (e.key === 'ArrowDown'){ active = Math.min(active+1, items.length-1); items.forEach((it,i)=>it.classList.toggle('active', i===active)); e.preventDefault(); }
      else if (e.key === 'ArrowUp'){ active = Math.max(active-1, 0); items.forEach((it,i)=>it.classList.toggle('active', i===active)); e.preventDefault(); }
      else if (e.key === 'Enter'){ if (active>=0 && matches[active]) selectCompany(matches[active]); }
      else if (e.key === 'Escape'){ clearSpotlight(); }
    });
    input.addEventListener('blur', () => setTimeout(() => list.classList.remove('open'), 120));
  }

  return {
    STATUS_ORDER, STATUS_LABEL_CLASS, COMPANIES,
    fmtPct, uniqueSorted,
    frequency, statusFrequency, crossTab, mode,
    showTip, hideTip,
    setupSlicers, setupCompanySearch,
  };
})();
