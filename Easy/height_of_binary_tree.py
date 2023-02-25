# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem?isFullScreen=true
def height(heroot):
	"""
	if you are a leaf return 0 else if you have to sons return max between sons + 1 else go to your only son.
	:param heroot: the root of the binary tree
	:return: length of the tree
	"""
	if heroot.left is None and heroot.right is None:
		return 0
	elif heroot.left and heroot.right:
		return 1 + max(height(heroot.left), height(heroot.right))
	elif heroot.left:
		return 1 + height(heroot.left)
	else:
		return 1 + height(heroot.right)
