# CVE-2023-2822-demo
Simple flask application to implement an intentionally vulnerable web app to demo CVE-2023-2822.

Based on the writeup at https://medium.com/@cyberninja717/reflected-cross-site-scripting-vulnerability-in-ellucian-ethos-identity-cas-logout-page-685bb1675dfb.

```
docker build -t xss-demo .
docker run -p <host_port>:5000 xss-demo
```

🤖 AIL LEVEL: This flask app's AI Influence Level is AIL4. 
- [The AIL Rating System](https://danielmiessler.com/blog/ai-influence-level-ail/)
- See [how this code was written](https://chat.openai.com/share/d5a85160-24d4-4451-b8c1-148fdca14a18)
