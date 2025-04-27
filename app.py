import gradio as gr
import shutil
import os

def get_image_paths(folder="_output"):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}
    image_paths = []
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)
        if os.path.isfile(item_path) and os.path.splitext(item)[1].lower() in image_extensions:
            image_paths.append(os.path.abspath(item_path))
    return image_paths

def move_file(file_path, folder_path="_output/good"):
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
    # margin-top: 200px;
css = """
footer { display: none !important; }
#btn-1 {
    background: #008170;
    height: 120px;
}
#btn-2 {
    background: #50727B;
    height: 120px;
}
#btn-3 {
    background: #8C6A5D;
    height: 120px;
}
"""

def fn_yeah_1(cur_cmp_image_path):
    move_file(cur_cmp_image_path, folder_path="_output/1")
    output_images = get_image_paths()
    if len(output_images) == 0: return "", None
    else: return output_images[0], output_images[0]

def fn_yeah_2(cur_cmp_image_path):
    move_file(cur_cmp_image_path, folder_path="_output/2")
    output_images = get_image_paths()
    if len(output_images) == 0: return "", None
    else: return output_images[0], output_images[0]

def fn_yeah_3(cur_cmp_image_path):
    move_file(cur_cmp_image_path, folder_path="_output/3")
    output_images = get_image_paths()
    if len(output_images) == 0: return "", None
    else: return output_images[0], output_images[0]

with gr.Blocks(title="IMAGEN", theme=theme, head=head, css=css, analytics_enabled=False) as demo:
    with gr.Row():
        with gr.Column():
            gr.Markdown()
        with gr.Column():
            cmp_image_show = gr.Image(None, interactive=False, show_label=False, show_download_button=False, show_fullscreen_button=False)
            cmp_image_path = gr.Text("", interactive=False, container=False)
        with gr.Column():
            cmp_btn_3 = gr.Button("⭐", elem_id="btn-3")
            cmp_btn_2 = gr.Button("⭐⭐⭐⭐", elem_id="btn-2")
            cmp_btn_1 = gr.Button("⭐⭐⭐⭐⭐", elem_id="btn-1")
    cmp_btn_1.click(fn=fn_yeah_1, inputs=[cmp_image_path], outputs=[cmp_image_path, cmp_image_show], show_progress="hidden")
    cmp_btn_2.click(fn=fn_yeah_2, inputs=[cmp_image_path], outputs=[cmp_image_path, cmp_image_show], show_progress="hidden")
    cmp_btn_3.click(fn=fn_yeah_3, inputs=[cmp_image_path], outputs=[cmp_image_path, cmp_image_show], show_progress="hidden")

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=1234, inbrowser=True, share=False)