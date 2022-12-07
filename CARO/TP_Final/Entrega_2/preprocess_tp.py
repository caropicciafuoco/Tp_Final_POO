def columns_type(df):
    return df.dtypes

def nans_por_columna(df):
    return df.isna().sum()

def producto_sucursal_unicos(df):
    df['prod-suc'] = df['producto_id'].astype(str) + "~" + df['sucursal_id'].astype(
        str)
    df = df.groupby('prod-suc', as_index = False).agg(precio = ("precio" ,"mean"))
    #df['aumento_precios'] = (((df['precio_mayo'] - df['precio_abril']) / df['precio_abril']) * 100).round(2)

    df[['producto_id', 'sucursal_id']] = df['prod-suc'].str.split('~',expand=True)
    df = df.drop(columns =['prod-suc'])
    return df


