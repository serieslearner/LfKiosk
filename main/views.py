from django.shortcuts import render, redirect
from django.http import  HttpResponseRedirect, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import base64
import io
import torchvision.transforms as transforms
import yolov5
from PIL import Image


@csrf_exempt
def process_photo(request):
    data = {'url': ""}
    print(request)
    if request.method == 'POST':
        encoded_image = request.POST['photo_data']
        image_data = encoded_image.split(',')[1]
        decoded_data = base64.b64decode(image_data)
        image_stream = io.BytesIO(decoded_data)
        photo_data = Image.open(image_stream)

        transform = transforms.Compose([
                transforms.Resize((640, 640)),
                transforms.ToTensor(),
        ])
        photo_tensor = transform(photo_data)
        model = yolov5.load('LfKiosk/best.pt')
        model.conf = 0.25
        model.iou = 0.45
        model.agnostic = False
        model.multi_label = False
        model.max_det = 1
        img = photo_data
        results = model(img)
        predictions = results.pred[0]
        boxes = predictions[:, :4]
        scores = predictions[:, 4]
        categories = str(predictions[:, 5])

        #print(str(categories))
        if (categories == 'tensor([1.])') | (categories == 'tensor([2.])') | (categories == 'tensor([3.])'):
            data = { 'url' : '/male_30/' }
        elif (categories == 'tensor([7.])') | (categories == 'tensor([8.])') | (categories == 'tensor([9.])'):
            data = { 'url' : '/female_30/' }
        elif (categories == 'tensor([4.])') | (categories == 'tensor([5.])') | (categories == 'tensor([6.])'):
            data = { 'url' : '/male_40/' }
        elif (categories == 'tensor([10.])') | (categories == 'tensor([11.])') | (categories == 'tensor([12.])'):
            data = {'url': '/female_40/'}
    response = JsonResponse(data, content_type='text/plain')
    return response


def index(request):
    return render(request, 'index.html')

def male_30_view(request):
    return render(request, 'Male30.html')

def male_40_view(request):
    return render(request, 'Male40.html')

def female_30_view(request):
    return render(request, 'Female30.html')

def female_40_view(request):
    return render(request, 'Female40.html')