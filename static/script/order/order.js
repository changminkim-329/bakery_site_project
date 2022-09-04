$(function() {
    console.log("click")
    $(".card > button").click(function() {
        var str1 = $(this).siblings('.card-title').html();
        var str2 = $(this).parents('.card-body').siblings('h3').html();
        var str4 = str1+"-"+str2;
        
        var condition = $(".order").parent('div').find('p').find("button").is("[class*="+str4+"]")
        console.log("[class*="+str4+"]"+"의 존재:"+condition);
        if(condition){
            var str3 = parseInt($("."+str4).siblings("span").html());
            
            if(str3>8){
                $("."+str4).siblings("span").html(9);
                console.log(str3);
                $("."+str4).siblings(".minus").html("-");
            }
            else{
                $("."+str4).siblings("span").html(str3+1);
                console.log(str3);
                $("."+str4).siblings(".minus").html("-");
            }
        }
        else{
            $(".purchase-list").append("<p><span class='purchase-number'>1</span> x " +str4+ "<button class='btn plus "+ str4+ "'>+</button><button class='btn minus "+ str4+"'>-</button></p><hr>");
        
        
            $(".plus."+str4).click(function(){
                var str3 = parseInt($(this).siblings("span").html());
                if(str3>8){
                    $(this).siblings("span").html(9);
                    $(this).siblings(".minus").html("-");
                }
                else{
                    $(this).siblings("span").html(str3+1);
                    $(this).siblings(".minus").html("-");
                }
                console.log(str4+"의 개수:"+str3);
            });

            $(".minus."+str4).click(function(){
                var str3 = parseInt($(this).siblings("span").html());
                if(str3-1<=0){
                    if($(this).html()=="x"){
                        console.log("삭제");
                        $(this).parent("p").siblings("hr").remove();
                        $(this).parent("p").remove();
                    }
                    $(this).html("x");
                }
                else{
                    $(this).html("-");
                    $(this).siblings("span").html(str3-1);
                }

                console.log(str4+"의 개수:"+str3);
            });
        }
        
        console.log(str4+" 주문 목록에 추가");
        
    });
    
    $(".order-button").click(function(){
        console.log("결제 실행");
    });
    
});