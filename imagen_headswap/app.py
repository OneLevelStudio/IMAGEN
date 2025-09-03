import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab("Create Mask"):
        with gr.Row():
            with gr.Column():
                gr.Markdown("")
            with gr.Column():
                gr.ImageEditor()
            with gr.Column():
                gr.Image()
            with gr.Column():
                gr.Markdown("")
    with gr.Tab("Tab 2"):
        gr.Markdown("Hello 2")
    with gr.Tab("Tab 3"):
        gr.Markdown("Hello 3")

if __name__ == "__main__":
    demo.launch(server_port=1235)