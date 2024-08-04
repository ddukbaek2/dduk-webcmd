# 알타바 API 관련 내용 정리

## 검수 대기 중인 모델 목록 조회.
- 요청:   
~~~
https://platform-api-{service}.altava.io/review/wait_list
~~~
- 응답:   
~~~
{
	"result": 100,
	"message": "success",
	"data": [
		{
			"id": "fe3a0966-634b-4b00-953d-9271cf465f53",
			"audit_config": "{"gender\":\"2\",\"category\":\"2\",\"vw\":\"roblox\",\"file_name\":\"TPCF465F53.fbx\",\"origin_vw\":\"altava\"}",
			"category": 2,
			"origin_vw": "altava"
		}
	]
}
~~~

## 검수 성공 요청.
- 요청:   
~~~
https://platform-api-{service}.altava.io/review/success/{design_id}
{
  "audit_config": "{\"gender\":\"2\",\"category\":\"301\",\"vw\":\"roblox\",\"file_name\":\"HA9A4726F2.fbx\",\"origin_vw\":\"altava\"}"
}
~~~

## 검수 실패 요청.
- 요청:   
~~~
https://platform-api-{service}.altava.io/review/fail/{design_id}
{
  "audit_text": "[
	{
		\"title\": \"Pivot error-Central axis\", 
		\"desc\": \"The object\"s central axis is not at (0,0,0).\",
		\"link\": \"https://docs.altava.com/creator-guide/modeling-guidelines/reset-pivot\"
	},
	{
		\"title\": \"Duplicated designs\",
		\"desc\": \"The file contains modeling or textures that have already been registered.\",
		\"link\": \"https://docs.altava.com/creator-guide/overview/overview\"
	}]"
}
~~~