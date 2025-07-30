class Widgets_Manager:
	def frames_constructoor(self, widgets_dict):
		created_widgets= {}
		for widgets_name, options in widgets_dict.items():
			parent = options.pop("parent")
			grid_options = {k:options.pop(k) for k in ["row","column","sticky"] if k in options}
			frame = tk.Frame(parent, **options)
			frame.grid(**grid_options)
			created_widgets[widget_name] = widget
