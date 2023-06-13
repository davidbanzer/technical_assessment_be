from rest_framework.views import APIView
from rest_framework.response import Response
import json


class ChessProblemView(APIView):
  
  def post(self,request):
    body = request.body.decode('utf-8')
    data = json.loads(body)
    n = data['n']
    k = data['k']
    rq = data['rq']
    cq = data['cq']
    obstacles = data['obstacles']
    attacks = self.queensAttack(n, k, rq, cq, obstacles)
    response = {
            'message': 'Queens attacks obtained',
            'data': {
                'attacks': attacks
            },
            'success': True
        }
    return Response(response)
  
  @staticmethod
  def queensAttack(n, k, rq, cq, obstacles):
      attacks = 0
      obstacle_set = set([(r, c) for r, c in obstacles])

      directions = [
          (-1, 0),  # Arriba
          (1, 0),   # Abajo
          (0, -1),  # Izquierda
          (0, 1),   # Derecha
          (-1, -1), # Diagonal superior izquierda
          (-1, 1),  # Diagonal superior derecha
          (1, -1),  # Diagonal inferior izquierda
          (1, 1)    # Diagonal inferior derecha
      ]

      for dr, dc in directions:
          r, c = rq, cq

          while True:
              # Moverse en la dirección actual
              r += dr
              c += dc

              if r < 1 or r > n or c < 1 or c > n or (r, c) in obstacle_set:
                  # Si se alcanza el borde del tablero o se encuentra un obstáculo, se detiene el movimiento
                  break

              # Se incrementa el contador de ataques
              attacks += 1

      return attacks







