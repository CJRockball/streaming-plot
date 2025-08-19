# Streaming Plot - Real-Time Data Visualization System

A comprehensive Python-based system for real-time data streaming and visualization using WebSockets, demonstrating live plotting capabilities with both Matplotlib and Bokeh frameworks.

## 🎯 Overview

This repository provides a complete real-time data visualization pipeline that simulates streaming financial data (stock prices) and displays it through interactive charts. The system demonstrates modern streaming architecture principles and real-time data processing techniques.

## 🏗️ Architecture

The system follows a **three-tier streaming architecture**:

```
┌─────────────────┐    WebSocket     ┌─────────────────┐    SQLite     ┌─────────────────┐
│   Data Source   │ ─────────────→   │  Data Storage   │ ────────────→ │  Visualization  │
│  (fake_data.py) │    Port 8766     │ (save2sql.py)   │   Database    │ (plot files)    │
└─────────────────┘                  └─────────────────┘               └─────────────────┘
```

## 📁 Project Structure

```
streaming-plot/
├── README.md                 # Project documentation
├── fake_data.py             # WebSocket server - generates synthetic stock data
├── save2sql.py              # WebSocket client - saves data to SQLite database  
├── matplotlib_plot.py       # Real-time plotting with Matplotlib
└── bokeh_plot.py           # Interactive plotting with Bokeh server
```

## 🔧 Core Components

### 1. Data Generation (`fake_data.py`)
- **Purpose**: WebSocket server that generates realistic stock price data
- **Algorithm**: Implements Geometric Brownian Motion for price simulation
- **Features**:
  - Realistic stock price movements with volatility
  - Configurable parameters (initial price, drift, volatility)
  - JSON-formatted data transmission
  - 50ms update interval for smooth real-time streaming

### 2. Data Persistence (`save2sql.py`)
- **Purpose**: Asynchronous WebSocket client for data storage
- **Features**:
  - Connects to WebSocket stream on `ws://localhost:8766`
  - Efficient batch processing with buffer management
  - Automatic SQLite database and table creation
  - Non-blocking asynchronous operations

### 3. Matplotlib Visualization (`matplotlib_plot.py`)
- **Purpose**: Real-time plotting with traditional Python visualization
- **Features**:
  - Live animation updates every 100ms
  - Rolling window display (maintains last 50 data points)
  - 15-period moving average calculation
  - Automatic axis scaling and formatting

### 4. Bokeh Visualization (`bokeh_plot.py`)
- **Purpose**: Interactive web-based plotting with Bokeh server
- **Features**:
  - Browser-based interactive charts
  - Auto-following x-axis for latest data
  - Server-side rendering for better performance
  - Real-time updates with 500ms interval

## 🚀 Quick Start

### Prerequisites
```bash
pip install asyncio websockets numpy matplotlib bokeh pandas sqlite3 aiosqlite
```

### Running the System

**Method 1: Complete Pipeline**
1. **Start the data generator** (Terminal 1):
   ```bash
   python fake_data.py
   ```

2. **Start the data storage service** (Terminal 2):
   ```bash
   python save2sql.py
   ```

3. **Launch visualization** (Terminal 3):
   ```bash
   # For Matplotlib visualization
   python matplotlib_plot.py
   
   # OR for Bokeh server visualization
   bokeh serve --show bokeh_plot.py
   ```

**Method 2: Bokeh Server Only**
```bash
bokeh serve --show bokeh_plot.py
```

## 🌟 Key Features

### Real-Time Data Processing
- **WebSocket Communication**: Efficient bidirectional communication
- **Asynchronous Operations**: Non-blocking data processing
- **Buffered Database Writes**: Optimized for high-frequency data

### Advanced Visualization
- **Dual Plotting Options**: Choose between Matplotlib and Bokeh
- **Interactive Charts**: Zoom, pan, and explore data (Bokeh)
- **Technical Indicators**: Moving average calculations
- **Responsive Design**: Auto-scaling and following latest data

### Financial Modeling
- **Geometric Brownian Motion**: Realistic price simulation
- **Configurable Parameters**: Adjust volatility and drift
- **Time-Series Analysis**: Historical data storage and retrieval

## 🛠️ Technical Implementation

### Data Flow
1. **Generation**: `fake_data.py` creates price data using GBM
2. **Transmission**: WebSocket sends JSON-formatted data
3. **Storage**: `save2sql.py` persists data to SQLite database
4. **Retrieval**: Plotting scripts query latest data
5. **Visualization**: Real-time chart updates

### Performance Optimization
- **Batch Processing**: Reduces database write operations
- **Rolling Windows**: Maintains memory efficiency
- **Asynchronous I/O**: Prevents blocking operations
- **Efficient Queries**: Optimized database access patterns

## 📊 Use Cases

This system demonstrates patterns applicable to:
- **Financial Trading Systems**: Real-time price monitoring
- **IoT Sensor Networks**: Live sensor data visualization  
- **System Monitoring**: Performance metrics dashboards
- **Social Media Analytics**: Live engagement tracking
- **Scientific Data Collection**: Laboratory measurement systems

## 🔄 Real-World Applications

The repository mentions a **real example** with "Live plotting of Bitcoin price from Binance", indicating the system can be adapted for actual cryptocurrency market data integration.

## 🎨 Visualization Comparison

| Feature | Matplotlib | Bokeh |
|---------|------------|-------|
| **Deployment** | Desktop application | Web browser |
| **Interactivity** | Limited | Full interactive |
| **Performance** | Good for desktop | Optimized for web |
| **Styling** | Traditional plots | Modern web interface |
| **Real-time Updates** | 100ms intervals | 500ms intervals |

## 🔍 Code Quality Features

- **Comprehensive Documentation**: Well-commented code
- **Error Handling**: Robust connection management
- **Modular Design**: Separated concerns architecture
- **Configurable Parameters**: Easy customization
- **Production Ready**: Scalable WebSocket implementation

## 📈 Future Enhancements

Potential improvements for this system:
- **Multiple Data Sources**: Support various financial APIs
- **Advanced Technical Indicators**: RSI, MACD, Bollinger Bands
- **Multi-Asset Support**: Portfolio-level visualization  
- **Authentication**: Secure WebSocket connections
- **Cloud Deployment**: Scalable infrastructure setup
- **Mobile Responsive**: Cross-platform compatibility

## 🤝 Contributing

This educational project demonstrates modern streaming architecture and real-time visualization techniques. The clean, modular codebase makes it an excellent foundation for learning and extension.

## 📄 License

Open source project available for educational and commercial use.

---

**Note**: This system provides an excellent foundation for understanding real-time data streaming, WebSocket communication, and modern visualization techniques in Python.