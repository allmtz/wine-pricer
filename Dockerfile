FROM node:16-alpine

WORKDIR /app

# Copy package.json
COPY package*.json ./

# Install root dependencies
RUN npm install

# Create and switch to a new user
RUN addgroup -S app && adduser -S app -G app

# Copy the project files into the container, change owner to 'app' user
COPY --chown=app:app . .

# Install Node.js dependencies for the client
RUN npm --prefix ./client install

# Switch to the non-root user
USER app

# Start the app
# The dev script exposes Vite on its default port
CMD ["npm", "run", "dev"]