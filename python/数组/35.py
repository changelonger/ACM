"""
����һ�����������һ��Ŀ��ֵ�����������ҵ�Ŀ��ֵ�������������������Ŀ��ֵ�������������У����������ᱻ��˳������λ�á�
����Լ������������ظ�Ԫ�ء�
numsΪ ���ظ�Ԫ�� �� ���� ��������
ʾ�� 1:

����: [1,3,5,6], 5
���: 2
ʾ�� 2:

����: [1,3,5,6], 2
���: 1
ʾ�� 3:

����: [1,3,5,6], 7
���: 4

ʾ�� 4:
����: [1,3,5,6], 0
���: 0
"""
def fun(nums,target):
    left,right = 0,len(nums)-1
    while left<=right:
        mid = left+(right-left)//2
        if nums[mid]<target:
            left = mid+1
        elif nums[mid]>target:
            right = mid-1
        else:
            return mid
    return left  #���� return right+1
    # ��Ϊleft�������right���ұߣ���target��ʱ����[right,left]�м�����Ҫ������棬return left������ return right+1