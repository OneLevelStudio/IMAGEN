import gradio as gr
import numpy as np
import shutil
import os

def fn_extract_from_editor(gr_imageeditor):
    if len(gr_imageeditor["layers"]) > 0:
        mask_binary = np.where(np.any(gr_imageeditor["layers"][0] != [0, 0, 0], axis=-1)[..., None], [255, 255, 255], [0, 0, 0]).astype(np.uint8)
        return mask_binary
    return None

def fn_update_download_button(gr_imagepreview):
    new_file_name = "2_facemask.jpg"
    if gr_imagepreview:
        new_file_path = os.path.join(os.path.dirname(gr_imagepreview), new_file_name)
        shutil.copy(gr_imagepreview, new_file_path)
        return gr.DownloadButton(label=f"Download {new_file_name}", value=new_file_path, visible=True)
    return None

# ====================================================================================================

theme = gr.themes.Base(
    primary_hue="slate",
    secondary_hue="slate",
    neutral_hue="neutral",
    radius_size="lg",
    font=[gr.themes.GoogleFont('Inter')], 
    font_mono=[gr.themes.GoogleFont('Ubuntu Mono')]
)
head = """
<link rel="icon" href="https://cdn.jsdelivr.net/gh/OneLevelStudio/CORE/STATIC/1LV_LOGO_DARK.png">
"""
css = """
* { -ms-overflow-style: none; scrollbar-width: none; }
*::-webkit-scrollbar { display: none; }
footer { display: none !important; }
"""

# ====================================================================================================

with gr.Blocks(title="FORGE Extra App", theme=theme, css=css, head=head, analytics_enabled=False) as demo:
    with gr.Tab("Create Mask"):
        with gr.Row():
            with gr.Column(min_width=1):
                gr.Markdown("")
            with gr.Column(min_width=640):
                gr_imageeditor = gr.ImageEditor(
                    show_label=False, show_fullscreen_button=False, height=720, show_download_button=False, interactive=True,
                    image_mode="RGB", type="numpy", format="jpeg",
                    placeholder="Upload an image", sources=('upload'), layers=False, canvas_size=(1080, 1350), brush=gr.Brush(colors=["#FF000080"], color_mode="fixed", default_size=100),
                )
            with gr.Column(min_width=640):
                gr_imagepreview = gr.Image(
                    show_label=False, show_fullscreen_button=False, height=720, show_download_button=False, interactive=False,
                    image_mode="RGB", type="filepath", format="jpeg",
                )
                gr_download = gr.DownloadButton(variant="primary", size="lg", visible=False)
            with gr.Column(min_width=1):
                gr.Markdown("")
    with gr.Tab("Tab 2"):
        gr.Markdown("Hello 2")
    with gr.Tab("Tab 3"):
        gr.Markdown("Hello 3")

    gr.on(
        triggers=gr_imageeditor.change,
        fn=fn_extract_from_editor,
        inputs=[gr_imageeditor],
        outputs=[gr_imagepreview],
        show_progress="hidden",
    ).then(
        fn=fn_update_download_button,
        inputs=[gr_imagepreview],
        outputs=[gr_download],
        show_progress="hidden",
    )

if __name__ == "__main__":
    demo.launch(server_port=1235)