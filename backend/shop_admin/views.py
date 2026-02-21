from django.http import JsonResponse
from .models import AutoScrollImage

def auto_scroll_images_api(request):
    """
    API endpoint returning all active auto scroll images, ordered by placement and order.
    Optionally filter by placement via query param: /api/scroll-images/?placement=top
    """
    placement_filter = request.GET.get('placement')
    
    queryset = AutoScrollImage.objects.filter(is_active=True).order_by('placement', 'order', '-created_at')
    
    if placement_filter:
        queryset = queryset.filter(placement=placement_filter)
        
    data = []
    for img in queryset:
        # Django Cloudinary Storage auto-resolves img.image.url
        data.append({
            'id': img.id,
            'title': img.title,
            'image_url': img.image.url if img.image else None,
            'placement': img.placement,
            'order': img.order
        })
        
    return JsonResponse({'status': 'success', 'data': data})
