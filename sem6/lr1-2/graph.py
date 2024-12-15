import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def read_marketing_data(file_path):
    df = pd.read_csv(file_path,
                     header=0,
                     names=['Date', 'Offline Spend', 'Online Spend'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.to_period('M')
    return df


def plot_monthly_sales(df):
    monthly_sales = df.groupby('Date')[['Offline Spend', 'Online Spend']].sum()
    monthly_sales = monthly_sales.sort_index(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    monthly_sales.plot(kind='barh',
                       stacked=True,
                       ax=ax,
                       color=['#1f77b4', '#ff7f0e'])

    for i, (idx, row) in enumerate(monthly_sales.iterrows()):
        offline = row['Offline Spend']
        online = row['Online Spend']
        total = offline + online
        ax.text(offline / 2,
                i,
                f'{int(offline)}',
                va='center',
                ha='center',
                color='white')
        ax.text(offline + online / 2,
                i,
                f'{online:.2f}',
                va='center',
                ha='center',
                color='white')
        ax.text(total + 100,
                i,
                f'{total:.2f}',
                va='center',
                ha='left',
                color='black')

    ax.set_ylabel('Month')
    ax.set_xlabel('Sales')
    ax.set_title('Monthly Offline and Online Sales')
    ax.set_yticks(range(len(monthly_sales)))
    ax.set_yticklabels([date.strftime('%m') for date in monthly_sales.index])
    ax.legend(['Offline Spend', 'Online Spend'])

    plt.tight_layout()
    plt.savefig('graph_1.png')
    plt.show()


def read_retail_data(file_path):
    data = pd.read_csv(file_path)
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
    return data


def plot_daily_sales(data):
    grouped = data.groupby(['InvoiceDate',
                            'StockCode'])['Quantity'].sum().reset_index()
    unique_dates = sorted(grouped['InvoiceDate'].unique())
    unique_stock_codes = grouped['StockCode'].unique()
    plot_data = pd.DataFrame(index=unique_dates, columns=unique_stock_codes)

    for _, row in grouped.iterrows():
        plot_data.at[row['InvoiceDate'], row['StockCode']] = row['Quantity']

    fig, ax = plt.subplots(figsize=(10, 6))

    for stock_code in unique_stock_codes:
        ax.scatter(plot_data.index, plot_data[stock_code], label=stock_code)

    ax.xaxis.set_major_locator(mdates.DayLocator(
        interval=30)) 
    ax.xaxis.set_major_formatter(
        mdates.DateFormatter('%Y-%m-%d')) 

    plt.title('Sales by Day')
    plt.xlabel('Date')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=-90)
    plt.legend(title='StockCode', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(False)
    plt.tight_layout()  
    plt.savefig('graph_2.png')
    plt.show()


marketing_data = read_marketing_data('MarketingSpend.csv')
plot_monthly_sales(marketing_data)

retail_data = read_retail_data('Retail.csv')
plot_daily_sales(retail_data)
