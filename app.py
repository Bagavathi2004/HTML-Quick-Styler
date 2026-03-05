import gradio as gr

def style_html(html_code):
    # Simple styling function
    styled_html = f"""
    <div style="font-family: Arial; padding:20px; background-color:#f4f4f4; border-radius:10px;">
        {html_code}
    </div>
    """
    return styled_html


with gr.Blocks() as app:
    gr.Markdown("# HTML Quick Styler")
    gr.Markdown("Enter HTML code and see the styled preview instantly.")

    html_input = gr.Textbox(
        label="Enter HTML Code",
        placeholder="<h1>Hello World</h1>",
        lines=10
    )

    output = gr.HTML(label="Styled Output")

    btn = gr.Button("Style HTML")

    btn.click(fn=style_html, inputs=html_input, outputs=output)


app.launch()