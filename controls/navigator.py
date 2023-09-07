import flet as ft


def navigator(page: ft.Page, selected_route: str):
    routes = {"/": 0, "/next_view": 1}

    async def change_route(e):
        route = list(routes.keys())[e.control.selected_index]
        await page.go_async(route)

    rail = ft.NavigationRail(
        selected_index=routes.get(selected_route, 0),
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.HOME, selected_icon=ft.icons.HOME_FILLED, label="首页"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="Next"
            )
        ],
        # on_change=lambda e: print(
        # "Selected destination:", e.control.selected_index),
        on_change=change_route
    )
    return rail
