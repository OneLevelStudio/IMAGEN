echo "📥 ==================================================================================================== 📥"

wget -P COMFY/models/diffusion_models https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W22_I2V_14B_HGH_FP8.safetensors
wget -P COMFY/models/diffusion_models https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W22_I2V_14B_LOW_FP8.safetensors
wget -P COMFY/models/text_encoders    https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/UMT5XXL_FP8.safetensors
wget -P COMFY/models/loras            https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W22_I2V_LX2V4S_HGH.safetensors
wget -P COMFY/models/loras            https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W22_I2V_LX2V4S_LOW.safetensors
wget -P COMFY/models/vae              https://huggingface.co/onelevelstudio/VIDGEN/resolve/main/WAN/W21_VAE.safetensors

echo "✅ ==================================================================================================== ✅"
