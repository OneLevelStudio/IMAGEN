import gradio as gr
import numpy as np

def fn_extract_from_editor(gr_mask_editor):
    if len(gr_mask_editor["layers"]) > 0:
        mask_binary = np.where(np.any(gr_mask_editor["layers"][0] != [0, 0, 0], axis=-1)[..., None], [255, 255, 255], [0, 0, 0]).astype(np.uint8)
        return gr_mask_editor["background"], mask_binary
    return gr_mask_editor["background"], None

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            gr_mask_editor = gr.ImageEditor(
                sources=['upload'],
                transforms=['crop'],
                image_mode="RGB", type="numpy", format="jpeg", show_fullscreen_button=False,
                layers=True,
                show_label=False,
                height=500,
                width=None,
                canvas_size=(1080, 1080),
                fixed_canvas=False,
                placeholder="Upload image",
                brush=gr.Brush(colors=["#FFFFFF84"], default_size=100, color_mode="fixed"),
                interactive=True,
            )
        with gr.Column():
            gr_image_preview = gr.Image(label="Input", image_mode="RGB", type="numpy", format="jpeg", show_fullscreen_button=False, height=300)
            gr_mask_preview  = gr.Image(label="Mask",  image_mode="RGB", type="numpy", format="jpeg", show_fullscreen_button=False, height=300)
        with gr.Column():
            gr.Markdown()

    gr.on(
        triggers=gr_mask_editor.change,
        fn=fn_extract_from_editor,
        inputs=[gr_mask_editor],
        outputs=[gr_image_preview, gr_mask_preview],
    )

if __name__ == "__main__":
    demo.launch()