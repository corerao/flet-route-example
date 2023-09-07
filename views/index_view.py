import asyncio

import flet as ft
from flet_route import Basket, Params

from controls.navigator import navigator


async def IndexView(page: ft.Page, params: Params, basket: Basket):
    await asyncio.sleep(2)

    async def handle_click(e):
        await page.go_async("/next_view")
    print(params)

    print(basket)
    return ft.View(
        route="/",
        controls=[
            ft.Row(
                [
                    navigator(page, "/"),
                    ft.VerticalDivider(width=1),
                    ft.Text("This Is Index View"), ft.ElevatedButton(
                        "Go Next View", on_click=handle_click),
                ], expand=True),]

    )
