import yfinance as yf

def obtener_cotizaciones():
    """
    Obtiene y muestra el costo actual de metales preciosos y divisas.
    """
    # Símbolos de mercado (Tickers) para los activos solicitados:
    # Divisas: El símbolo del dólar (USD) se usa como base para las otras divisas.
    # El resultado es el costo de 1 unidad de la divisa en USD (o la divisa base).
    # Para el Euro, se usa el par EUR/MXN (Euro a Peso Mexicano)
    # Para el Dólar, se usa el par USD/MXN (Dólar a Peso Mexicano)
    # Para el Yen, se usa el par JPY/MXN (Yen a Peso Mexicano)
    
    # Metales Preciosos: Los precios de los metales se cotizan comúnmente en USD por onza
    # En este ejemplo, usaremos el USD por Onza troy (OZ)
    # La plata (Silver) se cotiza como XAG=X (en USD por Onza)
    # El oro (Gold) se cotiza como XAU=X (en USD por Onza)
    
    # Nota: Los precios de metales en quilates (14k, 18k, etc.) no tienen un ticker
    # directo. Generalmente, se calculan como una fracción del precio del oro puro (XAU=X).
    
    activos = {
        "Dólar Estadounidense (USD/MXN)": "MXN=X",
        "Euro (EUR/MXN)": "EURMXN=X",
        "Yen Japonés (JPY/MXN)": "JPYMXN=X",
        "Oro Puro (XAU/USD)": "GC=F", # Futuro de Oro (el más usado para referencia)
        "Plata Pura (XAG/USD)": "SI=F" # Futuro de Plata
    }
    
    print("--- Cotizaciones de Mercado Actuales ---")
    
    for nombre, ticker in activos.items():
        try:
            # Descargar datos del ticker
            data = yf.Ticker(ticker)
            # Obtener el precio actual (cierre anterior o último precio disponible)
            cotizacion_raw = data.history(period="1d")
            
            if not cotizacion_raw.empty:
                # El precio se encuentra en la columna 'Close'
                precio = cotizacion_raw['Close'].iloc[-1]
                
                # Ajuste para mostrar el precio en Pesos o la moneda adecuada
                if "MXN" in ticker:
                    print(f"💰 {nombre}: {precio:,.4f} MXN (Peso Mexicano)")
                elif "XAU" in ticker or "GC=F" in ticker:
                    print(f"🥇 {nombre}: {precio:,.2f} USD (Dólares por Onza Troy)")
                    
                    # *Cálculo Estimado de Oro 14K:*
                    # El oro 14k es 58.3% oro puro (14/24 = 0.5833).
                    # Este es un cálculo teórico, no el precio de venta final.
                    precio_14k = precio * (14/24)
                    print(f"   (Est. Oro 14K/USD/Oz: {precio_14k:,.2f} USD)")
                    
                elif "XAG" in ticker or "SI=F" in ticker:
                    print(f"🥈 {nombre}: {precio:,.2f} USD (Dólares por Onza Troy)")
            else:
                print(f"❌ {nombre}: No se encontró cotización (Ticker: {ticker})")

        except Exception as e:
            print(f"⚠️ Error al obtener {nombre} ({ticker}): {e}")

if __name__ == "__main__":
    obtener_cotizaciones()
