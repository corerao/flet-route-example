import flet as ft
from flet_route import Basket, Params

from controls.navigator import navigator


async def NextView(page: ft.Page, params: Params, basket: Basket):
    async def handle_click(e):
        await page.go_async("/")
    print(params)
    print(basket)
    return ft.View(
        route="/next_view/:my_id",
        controls=[
            ft.Row(
                 [
                     navigator(page, "/next_view"),
                     ft.VerticalDivider(width=1),
                     ft.Text("This Is Next View"), ft.ElevatedButton(
                         "Go Next View", on_click=handle_click),
                 ], expand=True)
        ],
    )
