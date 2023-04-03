from django import template

register = template.Library()

@register.filter
def use_media(set, media_use):
    img_type, img_attr = media_use.split('.')
    try:
        # Change file.name to URL after implementing S3
        if set.model_name() == 'promo':
            media = set.media
        else:
            media = set.media.filter(media_use=img_type).first()
        
        if img_attr == 'src':
            return media.file.name
        elif img_attr == 'descr':
            return media.description
    except:
        return None