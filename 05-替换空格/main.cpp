class Solution {
public:
	void replaceSpace(char *str,int length) {
        int space_counts = 0;
        int origin_length = 0;
        for(int i = 0; i < length; i++){
            if (str[i] == '\0'){
                origin_length = i;
                break;
            }
            if (str[i] == ' '){
                space_counts++;
            }
        }
        int new_length = origin_length + 2 * space_counts;
        str[new_length] = '\0';
        for(int i = origin_length; i != 0; --i){
            if(str[i - 1] == ' '){
                str[new_length - 1] = '0';
                str[new_length - 2] = '2';
                str[new_length - 3] = '%';
                new_length -= 3;
            }
            else{
                str[new_length - 1] = str[i - 1];
                --new_length;
            }
        }


	}
};
