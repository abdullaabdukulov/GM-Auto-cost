from rest_framework.response import Response
from rest_framework.views import APIView
import numpy as np

# parameters
# 1. 'name' – malibu
# 2. 'engine size' – 185
# 3. 'curb weight' – 1531
# 4. 'horsepower' – 160
# 5. 'car width' – 69.2
# 6. 'drive wheels' - awd'
# 7. 'engine-location' – 'front'
# 8. 'price' predict
from api.apps import ApiConfig


class AutoCostPredict(APIView):
    def post(self, request):
        data = request.data
        name = data['name']
        engineSize = data['engine size']
        curbWeight = data['curb weight']
        horsePower = data['horsepower']
        carWidth = data['car width']
        driveWheels = data['drive wheels']
        engineLocation = data['engine-location']

        randomForest = ApiConfig.model
        summa = randomForest.predict([[engineSize, curbWeight, horsePower, carWidth, driveWheels, engineLocation]])[0]
        summa = np.round(summa)
        # print("%s %d$" % (name, summa))
        response_dict = {f'Predicted {name} ($)': summa}
        return Response(response_dict, status=200)



