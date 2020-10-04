class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        bool isUp = true, isDown = true;
        for( int i = 1; i < A.size(); ++i )
        {
            if( isUp == true || isDown == true )
            {
                if( A[i] > A[i-1] )
                {
                    isDown = false;
                }
                else if( A[i] < A[i-1] )
                {
                    isUp = false;
                }
            }
            else
            {
                break;
            }
        }
        if( isUp == false && isDown == false )
        {
            return false;
        }
        return true;
    }
};
