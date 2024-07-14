
# Using Python FastAPI for OpenAI Proxy
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FLyonLeopard%2Fopenai-proxy-vercel)
> If you are seeking a similar service deployed with Cloudflare Worker, you may want to try [openai-cloudflare](https://github.com/janlay/openai-cloudflare), which inspired this project.

### Compared with the original project
- This project is based on Python FastAPI and deployed on Vercel.
- This project simply forwards your OpenAI API requests through Vercel serverless. It does not offer any additional features beyond this basic function, and there are no plans to add more features.
- If you want more advanced features, you can try [openai-cloudflare](https://github.com/janlay/openai-cloudflare) instead

## Deploy
- Click the "Deploy with Vercel" button above.

## Usage
Replace the request url with your vercel domain.
E.g. the original url would be `https://api.openai.com/v1/foo`, you should replace it with `https://<your-vercel-domain>/v1/foo`.


## Chores
- I would suggest changing your Vercel deployment region to Washington or another location in the US.
- I would sugget your assign a custom domain to your Vercel deployment for faster (BTW, I remember that Vercel includes a CDN. Therefore, if you are using Cloudflare to set up the domain name, there is no need to enable the small cloud icon next to DNS.).

Enjoy the journey!