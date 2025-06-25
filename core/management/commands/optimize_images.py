from django.core.management.base import BaseCommand
from core.models import Image
from PIL import Image as PilImage
from django.core.files.base import ContentFile
import os
import io

class Command(BaseCommand):
    help = "Generate optimized WebP versions for existing images"

    def handle(self, *args, **options):
        for img_obj in Image.objects.all():
            if img_obj.images and not img_obj.optimized:
                self.stdout.write(f"Optimizing {img_obj.images.name}")
                pil_img = PilImage.open(img_obj.images.path)
                pil_img = pil_img.convert("RGB")
                if pil_img.width > 1280:
                    ratio = 1280 / float(pil_img.width)
                    height = int(float(pil_img.height) * ratio)
                    pil_img = pil_img.resize((1280, height), PilImage.Resampling.LANCZOS)
                buffer = io.BytesIO()
                pil_img.save(buffer, format="WEBP")
                filename = os.path.splitext(os.path.basename(img_obj.images.name))[0] + '.webp'
                img_obj.optimized.save(filename, ContentFile(buffer.getvalue()), save=True)
        self.stdout.write(self.style.SUCCESS('Optimization complete.'))
