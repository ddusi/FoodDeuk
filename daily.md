## 수정사항

0306 // detail 상세페이지 작성 시도. 

1. 상세페이지 url을 detail.html로 연동시켜서 ajax로 각 테이블 조회해여 뿌려주자...?

   ```python
   def detail(request, id):
       R = Restaurant.objects.all()
       context = {'Restaurant': R}
       return render(request, 'mainapp/detail.html', context)
   ```

   ```javascript
           $
             .ajax({
               url: '/swipe/load_likeornot/',
               type: 'GET',
               data: {
                 "latitude": 37.5015724,
                 "longitude": 127.0393363
               },
               success: function (res) {
     
                 var html = "";
                 var shtml = "";
     
                 // 				res[0~9].id/title/latitude/longitude
   
   
                 for (var i = res.length - 1; i > res.length - 9; i--) {
                   html += '<li class ="like_element">'
                   html += '<img class="img-fluid" src="'
                   html += res[i].fields.r_img
                   html += '" alt="">'
                   html += '</li>'
               }//for
               $('.like_list_container').append(html);
               
             }//success
           });//ajax
   ```

   

2. views.py에서 HttpResponse를 이용...???

   ```python
   def index(request):
       return HttpResponse(likeres_json, content_type='application/json')
   ```

   

   

