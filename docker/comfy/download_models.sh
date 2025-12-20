echo "===================================================================================================="
echo "===================================================================================================="
echo "===================================================================================================="

# wget -O COMFY/models/diffusion_models/W22_I2V_HGH.safetensors https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors
# wget -O COMFY/models/diffusion_models/W22_I2V_LOW.safetensors https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors
# wget -O COMFY/models/text_encoders/UMT5XXL.safetensors        https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
# wget -O COMFY/models/loras/W22_LX2V_HGH.safetensors           https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
# wget -O COMFY/models/loras/W22_LX2V_LOW.safetensors           https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
# wget -O COMFY/models/vae/W21_VAE.safetensors                  https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors

wget -P COMFY/models/diffusion_models "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/W22_I2V/W22_I2V_HGH.safetensors"
wget -P COMFY/models/diffusion_models "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/W22_I2V/W22_I2V_LOW.safetensors"
wget -P COMFY/models/text_encoders    "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/W22_I2V/UMT5XXL.safetensors"
wget -P COMFY/models/loras            "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/W22_I2V/W22_LX2V_HGH.safetensors"
wget -P COMFY/models/loras            "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/W22_I2V/W22_LX2V_LOW.safetensors"
wget -P COMFY/models/vae              "https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/W22_I2V/W21_VAE.safetensors"

echo "===================================================================================================="
echo "===================================================================================================="
echo "===================================================================================================="
