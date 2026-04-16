# Build stage
FROM node:18-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install

# Build env args can be updated to point to the live backend URL
COPY . .
RUN npm run build

# Serve stage
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 8080 specifically for Cloud Run
EXPOSE 8080

# Cloud Run deployment requires binding to PORT or utilizing custom nginx config
# Using a custom wrapper to replace the default nginx port
RUN sed -i 's/listen  *80;/listen 8080;/g' /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
