echo "===================================================================================================="
echo "===================================================================================================="
echo "===================================================================================================="

wget -P COMFY/models/diffusion_models http://37.27.250.71:8000/W22_I2V_14B_HGH_FP8.safetensors
wget -P COMFY/models/diffusion_models http://37.27.250.71:8000/W22_I2V_14B_LOW_FP8.safetensors
wget -P COMFY/models/text_encoders    http://37.27.250.71:8000/UMT5XXL_FP8.safetensors
wget -P COMFY/models/loras            http://37.27.250.71:8000/W22_I2V_LX2V4S_HGH.safetensors
wget -P COMFY/models/loras            http://37.27.250.71:8000/W22_I2V_LX2V4S_LOW.safetensors
wget -P COMFY/models/vae              http://37.27.250.71:8000/W21_VAE.safetensors

echo "===================================================================================================="
echo "===================================================================================================="
echo "===================================================================================================="

# wget -P COMFY/models/diffusion_models https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W22_I2V_14B_HGH_FP8.safetensors
# wget -P COMFY/models/diffusion_models https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W22_I2V_14B_LOW_FP8.safetensors
# wget -P COMFY/models/text_encoders    https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/UMT5XXL_FP8.safetensors
# wget -P COMFY/models/loras            https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W22_I2V_LX2V4S_HGH.safetensors
# wget -P COMFY/models/loras            https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W22_I2V_LX2V4S_LOW.safetensors
# wget -P COMFY/models/vae              https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W21_VAE.safetensors

# wget -P COMFY/models/diffusion_models https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors
# wget -P COMFY/models/diffusion_models https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors
# wget -P COMFY/models/text_encoders    https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors
# wget -P COMFY/models/loras            https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
# wget -P COMFY/models/loras            https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
# wget -P COMFY/models/vae              https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors
