"""Patch only the two reviewed UI state paths; preserve each input's other code."""


def patch_ui(raw: bytes) -> bytes:
    text = raw.decode('utf-8')
    newline = '\r\n' if b'\r\n' in raw else '\n'

    def replace(old, new):
        nonlocal text
        if text.count(old) != 1:
            raise ValueError('UI patch input differs from the reviewed source: ' + old[:100])
        text = text.replace(old, new)

    anchor = "function resetMainSearch(value=''){mainSearch?.reset();appliedSearch=value.toLowerCase();$('search').value=value;clearFacetSections();}"
    replace(anchor, anchor + newline + '  // Explicit navigation starts a new view; same-route reload keeps its saved query.' + newline + '  function resetRouteSearch(){resetMainSearch();page=1;restoredScrollY=0;}')
    guard = "if(demoMode&&prefs.catalogView==='style'){"
    if guard in text:
        replace(guard, "if(demoMode&&prefs.catalogView==='style'&&!(requestedTab==='styles'&&prefs.route===location.search)){")
    for branch in ["else if(run){", "else if(requestedTab==='creatures'){", "else if(new URLSearchParams(location.search).get('category')==='chinese-animation'){", "else if(new URLSearchParams(location.search).get('category')==='kyoto-animation'){", "else if(requestedTab==='styles'){"]:
        replace(branch, branch + 'resetRouteSearch();')
    replace('const scrollTop=virtual?Math.max(0,Math.min(list.scrollTop,Math.max(0,total*rowHeight-viewport))):list.scrollTop;',
            '// Empty lists have no scroll range yet; keep the saved offset until rows exist.' + newline + '    const savedScroll=list.children.length?list.scrollTop:state.scrollTop||0;' + newline + '    const scrollTop=virtual?Math.max(0,Math.min(savedScroll,Math.max(0,total*rowHeight-viewport))):savedScroll;')
    replace('list.scrollTop=scrollTop;state.scrollTop=scrollTop;', 'list.scrollTop=scrollTop;state.scrollTop=list.scrollTop;')
    replace('state.search=search;state.list=list;list.scrollTop=state.scrollTop;', 'state.search=search;state.list=list;')
    return text.encode('utf-8')
