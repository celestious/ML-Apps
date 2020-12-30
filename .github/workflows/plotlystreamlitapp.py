


	elif choice == "Plotly":
		st.subheader("Automated EDA with Plotly")
		data_file = st.file_uploader("Upload CSV", type=['csv'])
		def load_data():
			df = pd.read_csv(data_file)
			numeric_df =df.select_dtypes(['float', 'int'])
			numeric_cols = numeric_df.columns
			text_cols = text_df.columns
			df, numeric_cols, text_cols = load_data()
			return df, numeric_cols, text_cols
			st.title("Here is your dashboad")
			st.write(df)
			# add checkbox to sidebar
			check_box = st.sidebar.checkbox(label="Display datasets")
			if check_box:
				st.write(df)
		st.sidebar.title("settings")
		feature_selection = st.sidebar.multiselect(label="select features to plot, options=numeric_cols")
		#select_dropdown= st.sidebar.selectbox()
		print(feature_selection)
		#df = df[df['Name']== stock_dropdown]
		df_features = df[feature_selection]

		plotly_figure = px.line(data_frame=df_features, x=df_features.index, y=feature_selection, title=(str(stock_dropdown) + ' ' +'timeline')
		# to display pltly chart we call plotly function in streamlit
		st.plotly_chart(plotly_figure)