import math


def make_pagination_range(
    page_range,
    qty_paginas,
    current_page,
):
    middle_range = math.ceil(qty_paginas / 2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total = len(page_range)
    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset
    if stop_range >= total:
        start_range = start_range-abs(total-stop_range)
    pag = page_range[start_range:stop_range]
    return {
        'pag': pag,
        'stop_range': stop_range,
        'start_range': start_range,
        'middle_range': middle_range,
        'total': total,
        'page_range': page_range,
        'qty_paginas': qty_paginas,
        'current_page': current_page,
        'first': current_page > middle_range,
        'last': stop_range < total

    }
