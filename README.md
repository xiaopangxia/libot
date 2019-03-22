# libot
A robot for library QA.


**Libot后端接口说明**

1.  请求方式POST

2.  请求地址：39.108.80.74：8888

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
		&emsp;&emsp;&emsp;“search_answer”:[<br>
&emsp;&emsp;&emsp;&emsp;[“相似问题1”，“相似问题1的答案”，“问题1相似度”]，<br>
&emsp;&emsp;&emsp;&emsp;[“相似问题2”，“相似问题2的答案”，“问题2相似度”]，<br>
&emsp;&emsp;&emsp;&emsp;[“相似问题3”，“相似问题3的答案”，“问题3相似度”]<br>
&emsp;&emsp;&emsp;&emsp;]<br>
&emsp;&emsp;}<br>
&emsp;c)	All:<br>
&emsp;&emsp;{<br>
&emsp;&emsp;&emsp;“search_answer”:[<br>
&emsp;&emsp;&emsp;&emsp;[“相似问题1”，“相似问题1的答案”，“问题1相似度”]，<br>
&emsp;&emsp;&emsp;&emsp;[“相似问题2”，“相似问题2的答案”，“问题2相似度”]，<br>
&emsp;&emsp;&emsp;&emsp;[“相似问题3”，“相似问题3的答案”，“问题3相似度”]<br>
&emsp;&emsp;&emsp;]，<br>
				&emsp;&emsp;&emsp;“graph_answer”:”回答字符串”<br>
&emsp;&emsp;}<br>


6.  截图

![](media/41a6b4136d4debc3127a7cd079873a87.png)

![](media/0a91c15fbea28dc98ed93d68421b261c.png)

![](media/c123ee8387432412dead036b0d0fcc5e.png)


