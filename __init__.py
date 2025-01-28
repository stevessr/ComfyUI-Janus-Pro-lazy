from .nodes.model_loader import JanusModelLoader
from .nodes.image_understanding import JanusImageUnderstanding
from .nodes.image_understanding2 import JanusImageUnderstanding2
from .nodes.image_generation import JanusImageGeneration
from .nodes.image_generation2 import JanusImageGeneration2

NODE_CLASS_MAPPINGS = {
    "JanusModelLoader": JanusModelLoader,
    "JanusImageUnderstanding": JanusImageUnderstanding,
    "JanusImageUnderstanding2": JanusImageUnderstanding2,
    "JanusImageGeneration": JanusImageGeneration,
        "JanusImageGeneration2": JanusImageGeneration2,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "JanusModelLoader": "Janus Model Loader",
    "JanusImageUnderstanding": "Janus Image Understanding",
    "JanusImageGeneration": "Janus Image Generation",
    "JanusImageUnderstanding2": "Janus 图像理解自定义节点",
    "JanusImageGeneration2": "Janus 图像生成自定义节点",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS'] 