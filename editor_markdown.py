import flet as ft


def main(page: ft.Page):

    def update_view(e):
        view.value = e.control.value
        view.update()

    page.padding=ft.padding.all(0)
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Editor Markdown"

    editor = ft.TextField(
        multiline=True,
        min_lines=20,
        max_lines=20,
        color='black',
        content_padding=30,
        border=ft.InputBorder.NONE,
        bgcolor=ft.colors.BLUE_GREY,
        on_change=update_view
    )

    how_to = ft.Container(
        expand=True,
        padding=ft.padding.all(30),
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            controls=[
                ft.Divider(color='grey', height=40),
                ft.Text(value="Para criar Títulos", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value="# H1", color='grey700'),
                ft.Text(value="## H2", color='grey700'),
                ft.Text(value="### H3", color='grey700'),
                ft.Text(value="...", color='grey700'),
                ft.Divider(color='grey', height=40),

                ft.Text(value="Para formatar textos", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value="__texto em negrito__", color='grey700'),
                ft.Text(value="*texto itálico*", color='grey700'),
                ft.Text(value="*__texto em negrito e itálico__*", color='grey700'),
                ft.Text(value="~~texto tachado~~", color='grey700'),
                ft.Divider(color='grey', height=40),

                ft.Text(value="Para criação de listas", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value=" - Não ordenda", color='grey700'),
                ft.Text(value=" 1. Ordenada", color='grey700'),
                ft.Divider(color='grey', height=40),

                ft.Text(value="Para inserir links e imagens", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value="[texto do link](url do link)", color='grey700'),
                ft.Text(value="![Texto da imagem](image.jpg)", color='grey700'),
                ft.Divider(color='grey', height=40),

                ft.Text(value="Para inserir código", weight=ft.FontWeight.BOLD, color='black'),
                ft.Text(value="`print(Código em uma linha)`", color='grey700'),
                ft.Text(value="```python\nprint('Código em múltiplas linhas')\n```", color='grey700'),
                ft.Divider(color='grey', height=40),
            ],
            spacing=10
        )
    )

    view = ft.Markdown(
        value=editor.value,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme='monokai-sublime',
        on_tap_link= lambda e: page.launch_url(e.data),
    )

    layout = ft.Row(
        expand=True,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.colors.WHITE,
                content=ft.Column(
                    controls=[
                        editor,
                        how_to
                    ]
                )
            ),
            ft.Container(
                expand=True,
                bgcolor=ft.colors.BLACK,
                padding=ft.padding.all(30),
                content=view,
            ),
        ],
        spacing=0
    )

    page.add(layout)


if __name__=='__main__':
    ft.app(target=main)