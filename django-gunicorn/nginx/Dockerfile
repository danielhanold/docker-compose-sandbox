FROM nginx:1.11

# Remove default nginx configuration file.
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d
