from flask import Flask

app = Flask(__name__)
  

def show_file():
     return '''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Пример формы</title>
                      </head>
                      <body>
                        <h1 Align=center>Пейзажи Марса</h1>
                        <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                          <div class="carousel-inner">
                            <div class="carousel-item active">
                              <img src="static/img/one.jpg" class="d-block w-100" alt="1">
                            </div>
                            <div class="carousel-item">
                              <img src="static/img/two.jpg" class="d-block w-100" alt="2">
                            </div>
                            <div class="carousel-item">
                              <img src="static/img/three.jpg" class="d-block w-100" alt="3">
                            </div>
                            <div class="carousel-item">
                              <img src="static/img/four.jpg" class="d-block w-100" alt="4">
                            </div>
                            <div class="carousel-item">
                              <img src="static/img/five.jpg" class="d-block w-100" alt="5">
                            </div>
                          </div>
                          <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-bs-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Previous</span>
                          </a>
                          <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-bs-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="visually-hidden">Next</span>
                          </a>
                        </div>
                      </body>
                    </html>'''                      
                        

@app.route('/carousel')
def carousel():
    return show_file()

                        
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')