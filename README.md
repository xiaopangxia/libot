# Libot，A robot for library QA.
# 图书馆智能咨询机器人


**Libot后端接口说明**

1.  请求方式POST

2.  请求地址：xxx.xxx.xxx.xxx:8888

3.  url参数说明：

    1.  target=graph_qa，知识库问答

    2.  target=search_qa，检索式问答

    3.  target=all， 调用所有现有问答方案


4.	json请求参数说明：<br>
&emsp;{<br>
&emsp;&emsp;“question”: “问题字符串”<br>
&emsp;}
5.	返回json格式说明：<br>
&emsp;a)	Graph_QA:<br>
&emsp;&emsp;{
		&emsp;&emsp;&emsp;“graph_answer”:”回答字符串”
&emsp;&emsp;}<br>
&emsp;b)	Search_qa:<br>
&emsp;&emsp;{<br>
&emsp;&emsp;&emsp;    "search_answer": [<br>
&emsp;&emsp;&emsp;&emsp;        {
            "question": "相似问题1", "score": "0.0", "answer": "相似问题1的答案"
        },<br>
&emsp;&emsp;&emsp;&emsp;        {
            "question": "相似问题2", "score": "0.0", "answer": "相似问题2的答案"
        },<br>
&emsp;&emsp;&emsp;&emsp;        {
            "question": "相似问题3",
            "score": "0.0",
            "answer": "相似问题3的答案"
        }<br>
&emsp;&emsp;&emsp;    ]<br>
&emsp;&emsp;}<br>

&emsp;c)	All:<br>
&emsp;&emsp;{<br>
&emsp;&emsp;&emsp;    "search_answer": [<br>
&emsp;&emsp;&emsp;&emsp;        {
            "question": "相似问题1", "score": "0.0", "answer": "相似问题1的答案"
        },<br>
&emsp;&emsp;&emsp;&emsp;        {
            "question": "相似问题2", "score": "0.0", "answer": "相似问题2的答案"
        },<br>
&emsp;&emsp;&emsp;&emsp;        {
            "question": "相似问题3",
            "score": "0.0",
            "answer": "相似问题3的答案"
        }<br>
&emsp;&emsp;&emsp;    ]，<br>
				&emsp;&emsp;&emsp;“graph_answer”:”回答字符串”<br>
&emsp;&emsp;}<br>
6.  截图

![](https://raw.githubusercontent.com/xiaopangxia/libot/master/image/request_graph.png)
![](https://raw.githubusercontent.com/xiaopangxia/libot/master/image/request_search.png)
![](https://raw.githubusercontent.com/xiaopangxia/libot/master/image/request_all.png)


