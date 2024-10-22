FROM node:16-alpine

WORKDIR /app

# Copy package.json
COPY package*.json ./

# Install root dependencies
RUN npm install

# Copy the project files into the container
COPY . .

# Install Node.js dependencies for the client
RUN npm --prefix ./client install

# Start the app
CMD ["npm", "run", "dev"]