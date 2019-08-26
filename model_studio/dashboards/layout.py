html_layout = '''<!DOCTYPE html>
                    <html>
                        <head>
                            {%metas%}
                            <title>{%title%}</title>
                            {%favicon%}
                            {%css%}
                        </head>
                        <body>
                            <section>
                                <nav>
                                    <h2>Model Studio</h2>
                                </nav>
                            </section>
                            <br>

                            <section>
                                {%app_entry%}
                            </section>
                            <footer>
                                {%config%}
                                {%scripts%}
                                {%renderer%}
                            </footer>
                        </body>
                    </html>'''
