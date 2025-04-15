import gradio as gr
import shutil
import os

def get_image_paths(folder="output"):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    image_paths = []
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path) and os.path.splitext(item)[1].lower() in image_extensions:
            image_paths.append(os.path.abspath(item_path))
    return image_paths

def move_file(file_path, folder_path):
    if file_path.strip() != "" and folder_path.strip() != "":
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path, exist_ok=True)
        file_name = os.path.basename(file_path)
        new_path = os.path.join(folder_path, file_name)
        shutil.move(file_path, new_path)


theme = gr.themes.Base(
    primary_hue="neutral",
    secondary_hue="neutral",
    neutral_hue="neutral",
    font=[gr.themes.GoogleFont('Inter')], 
    font_mono=[gr.themes.GoogleFont('Ubuntu Mono')]
)
head = """
<link rel="icon" href="https://cdn.jsdelivr.net/gh/OneLevelStudio/CORE/static/favicon.png">
"""

def fn_yeahhhhh(cur_cmp_image_path):
    
    move_file(cur_cmp_image_path, "output/good")

    output_images = get_image_paths()
    if len(output_images) == 0:
        return "", None
    else:
        return output_images[0], output_images[0]

with gr.Blocks(title="IMAGEN", theme=theme, head=head, analytics_enabled=False) as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown("1")
        with gr.Column():
            cmp_image_path = gr.Text("", interactive=False)
            cmp_image_show = gr.Image(None, interactive=False)
        with gr.Column():
            cmp_btn_1 = gr.Button("Good")
    cmp_btn_1.click(fn=fn_yeahhhhh, inputs=[cmp_image_path], outputs=[cmp_image_path, cmp_image_show])

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1", 
        server_port=1234, 
        inbrowser=True,
        enable_monitoring=True,
        strict_cors=True,
    )