# 트리
* 비선형구조
* 나무를 거꾸로 한 것과 비슷해서 트리라고 말한다.

***

## 트리의 용어 설명
### 트리의 모든 노드는 자신의 서브트리의 루트노드이다.
* 루트노드: 최상의 루트노드는 A(가장 최상위)이고, B(나, 서브트리)
* 간선 또는 에지: 모든 노드가 선으로 연결되어 있기 때문에, 모든 노드를 간선 또는 엣지라고 말한다.
* 부모/자식/형제: 자신의 서브노드로 직접적으로 연결되어 있고, 형제노드의 경우 같은 depth에 있는 노드를 형제노드라고 한다.
* 조상/자손: B의 자손 노드는 '나'와 연결되어있는 모든 노드로, 해당 노드 아래에 있는 모든 노드를 자손으로 말한다. 또한 조상노드의 경우 '하나'만 해당되는게 아니라, 자신을 기준으로 직계로 연결되어 있는 노드들을 말한다. 주변노드는 포함되지 않는다.
* 단말/비단말 노드: 2레벨이든 3레벨이든 레벨과 상관없이 자기와 관련있는 아래의 서브노드가 없을 경우 끝에 있는 노드라고 해서, '단말'노드라고 한다. 그 반대는 비단말노드라고 한다.
* 노드의 차수: 각 노드에 연결되어 잇는 간선 또는 엣지. 예를 들어 A에 대해서 직접적으로 연결되어 있는 노드들이 차수라고 한다.
* 트리의 차수: 각 노드의 차수들 중에서 가장 큰 차수를 말한다. 노드기리의 차수중에서 가장 큰 것. 한 공간에서 5개의 차수를 가지는 곳이 있다면 위치에 상관없이 트리의 차수가 5라고 말한다.
* 레벨: depth를 말한다. 하위로 내려갈수록 레벨(단위)수가 높다.
* 트리의 높이: 전체 안에서 단계가 얼마나 있는지를 말한다. 4개 레벨까지 있으면 트리 높이가 4라고 하면 된다.
* 포리스트(forest): 

## 일반 트리의 표현 방법
### 일반 트리의 노드
선형으로 연결된다. 선은 하나로 계속 옆으로 이어서 붙여줄 수 있다.

### 다른 방법
자식 노드와 연결하는 노드와, 다음 형제 노드와 연결하는 노드가 필요하다. 따라서 연결포인터가 두개 필요하다.

***
## 이진트리
모든 노드가 2개의 서브트리를 갖는 트리를 말한다.
* 서비트리는 공집합일 수 있다.
* 이진트리는 순환적으로 정의된다.
* 이진트리는 비어있거나, 비어있지(empty) 않으면, 루트노드와 2개의 이진트리인 왼쪽 서브트리와 오른쪽 서브트리로 구성된다

### 이진 트리의 분류
#### 포화 이진트리(full binary tree)
트리의 각 레벨에 노드가 꽉 차있는 이진트리, 그래서 무조건 트리 하나 당 자식이 두개씩 있어야 한다.

* 노드의 번호 : depth 맞는 것들 순서대로 번호를 지정하고 해당 레벨이 끝나고 나면 다음 레벨로 넘어가야 한다. 또한 번호는 왼쪽에서 오른쪽으로  진행된다.

#### 완전 이진트리(complete binary tree)
포화 이진트리보다는 노드가 덜 찼다고 볼 수 있는데, 높이가 h일 때, h-1(깊이)까지는 노드가 모두 채워진다. 마지막 레벨 h, 가장 높은 레벨에서는 노드가 순서대로 채워진다.

#### 기타 이진트리
완전, 포화 이진트리가 아니다. 왼쪽 또는 오른쪽의 노드가 비어있다. 중간에 빈 노드가 있으면 안되기 때문에, 그냥 이진트리라고 볼 수 있다.


## 이진트리의 성질
* 노드의 갯수가 n개이면 간선의 갯수는 n-1이다.
* 높이가 h이면 h ~ 2의 h승 - 1개의 노드를 가진다 (최대 노드수)
* n개 노드의 이진 트리 높이: [log2(n + 1)] ~ n

## 이진트리의 탐색
* 왼쪽부터 탐색하면 된다. 만약 링크가 없어 단말노드일 경우 None으로 표현하면 된다.리의 표현
### 배열 표현법

### 링크 표현법
* 왼쪽 자식 - data - 오른쪽 자식
* 링크는 자식노드만 연결시키면 된다.
* 탐색의 순서는 왼쪽에서 오른쪽으로
* 최초의 탐색 기준을 찾을 때에는 시작 포인트를 찾으면 되는데, 시작점은 '최상위'를 기준으로 하여서, root pointer를 찾으면 된다. 그러고 나면 그 다음 자식 노드를 찾으면 되기 떄문. 왼쪽부터 탐색하면 된다.
* 만약 링크가 없어 단말노드일 경우 None으로 표현하면 된다.

## 이진트리의 연산
### 순회
* 트리에 속하는 모든 노드를 한 번씩 방문하는 것
* 선형 자료구조는 순회가 단순하다. 구조 자체가 선형이기 때문임
* 트리는 다양한 방법이 있다. 

### 이진트리의 기본 순회는 3가지
* 전위 순회(preorder traversal) : VLR, 루트노드를 처음에 탐색함
* 중위 순회(inorder traversal) : LVR, 루트노드를 중간에 탐색함
* 후위 순회(postorder traversal) : LRV, 루트노드를 마지막에 탐색함

    -> 루트노드를 언제 탐색하냐에 따라 탐색방법이 달라짐


* 순회 또한 왼쪽 먼저, 오른쪽 그다음
* 전체나 서브트리나 구조는 동일하다. 

### 1) 전위순회
* 루트 -> 왼쪽 서브트리 먼저 -> 오른쪽 서브트리를 그 다음
* 서브트리 내에서도 루트 먼저 탐색, 전체가 같은 방식으로 순회함

```python
def preorder(n):
    if n is not None:
        print(n.data, end='')
        preorder(n.left)
        preorder(n.right)
```

### 2) 종위순회
* 왼쪽 서브트리 -> 루트 -> 오른쪽 서브트리
```python
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end='')
        inorder(n.right)
```

### 3) 후위순회
* 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트 
```python
def postorder(n):
    postorder(n.left)
    postorder(n.right)
    print(n.data, end='')
```

### 4) 레벨순회
* 노드를 레벨 순으로 검사하는 순회 방법
    * 큐를 사용해 구현
    * 순환을 사용하지 않음
    

* 너비우선 탐색과 유사하기 때문에 갈수록 양이 늘어남
```python
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
        print(n.data, end='')
        queue.enqueue(n.left)
        queue.enqueue(n.right)
```

## 이진트리 연산
### 노드 개수, 단말 노드의 수
### 1) 노드 개수
```python
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)
```

### 2) 단말 노드의 수
```python
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)
```

### 3) 트리 높이
```python
def cal_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if(hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1
```