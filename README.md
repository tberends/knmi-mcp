# KNMI Weather MCP

A FastMCP server that provides real-time weather data from KNMI (Royal Netherlands Meteorological Institute) weather stations. This application fetches the latest 10-minute measurements from the nearest weather station to any location in the Netherlands.

<a href="https://glama.ai/mcp/servers/xanerdcjsm">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/xanerdcjsm/badge" alt="KNMI Weather MCP server" />
</a>

## Features

- Get weather data for any location in the Netherlands
- Automatically finds the nearest KNMI weather station
- Provides real-time measurements including:
  - Temperature
  - Humidity
  - Wind speed and direction
  - Precipitation
  - Visibility
  - Air pressure
  - Cloud cover
- Natural language interpretation of weather conditions
- Location search functionality
- Detailed logging

## Prerequisites

- Python 3.10 or higher
- KNMI API Key (get one from [KNMI Data Platform](https://dataplatform.knmi.nl/))
- `uv` package manager

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd knmi-mcp
   ```

2. Create a `.env` file in the project root:
   ```bash
   KNMI_API_KEY=your_api_key_here
   ```

## Running the Server

### Using Claude AI

To use this application with Claude AI, follow these steps:

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Add configuration to Claude:**
   Manually add the following configuration to your Claude configuration file (typically located at `~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "KNMI Weather": {
      "command": "/Users/<username>/<git location>/knmi-mcp/.venv/bin/python",
      "args": [
        "/Users/<username>/<git location>/knmi-mcp/src/knmi_weather_mcp/server.py"
      ],
      "cwd": "/Users/<username>/<git location>/knmi-mcp"
    }
  }
}
```

**Note:** Replace `/Users/<username>/<git location>/knmi-mcp` with the actual path to your project directory.

**Important:** Make sure you have installed the dependencies first by running:

```bash
uv sync
```

This will create the virtual environment and install all required dependencies.

### Manual Running

For development or standalone usage:

```bash
uv run fastmcp run src/knmi_weather_mcp/server.py
```

## Available Tools

### 1. what_is_the_weather_like_in

Get a natural language interpretation of current weather conditions for any location in the Netherlands.

Example:

```python
await what_is_the_weather_like_in("Amsterdam")
```

### 2. get_location_weather

Get raw weather data for a location.

Example:

```python
await get_location_weather("Rotterdam")
```

### 3. search_location

Search for locations in the Netherlands.

Example:

```python
await search_location("Utrecht")
```

### 4. get_nearest_station

Find the nearest KNMI weather station to given coordinates.

Example:

```python
await get_nearest_station(52.3676, 4.9041)
```

## Configuration

The application uses environment variables for configuration:

- `KNMI_API_KEY`: Your KNMI API key (required)
- `PORT`: Server port (default: 8001)

All dependencies are automatically managed by the FastMCP server, including:
- httpx
- pydantic
- python-dotenv
- pandas
- xarray
- numpy
- netCDF4

## Logging

The application logs are stored in the `logs/knmi_weather.log` file, providing detailed information about:

- API requests and responses
- Weather data processing
- Error messages
- Debug information

## Data Sources

This application uses the KNMI Data Platform API to fetch data from the "10-minute-in-situ-meteorological-observations" dataset, which provides 10-minute interval measurements from all KNMI automatic weather stations in the Netherlands.

## Error Handling

The application includes robust error handling for:

- Invalid locations
- API authentication issues
- Network problems
- Data parsing errors
- Missing measurements