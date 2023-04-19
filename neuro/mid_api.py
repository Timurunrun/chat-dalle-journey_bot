import os
import replicate

def generate_image(prompt):
    os.environ['REPLICATE_API_TOKEN'] = 'b45d4db61c88f8831df9c4e5c678600cd87aa45f'
    model = replicate.models.get('prompthero/openjourney')
    version = model.versions.get('9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb')
    
    inputs = {
        'prompt': prompt,
        'width': 512,
        'height': 512,
        'num_outputs': 4,
        'num_inference_steps': 50,
        'guidance_scale': 6
    }

    output = version.predict(**inputs)
    return(output)

def upscale_image(prompt):
    os.environ['REPLICATE_API_TOKEN'] = 'b45d4db61c88f8831df9c4e5c678600cd87aa45f'
    model = replicate.models.get('nightmareai/real-esrgan')
    version = model.versions.get('42fed1c4974146d4d2414e2be2c5277c7fcf05fcc3a73abf41610695738c1d7b')

    inputs = {
        'image': prompt,
        'scale': 4,
        'face_enhance': False
    }

    output = version.predict(**inputs)
    return(output)
