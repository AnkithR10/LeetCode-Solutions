

char * defangIPaddr(char * address){
    int len = strlen(address);
    char *result = (char *)malloc(len + 7); 
    int j = 0;
    for (int i = 0; i < len; i++) {
        if (address[i] == '.') {
            result[j++] = '[';
            result[j++] = '.';
            result[j++] = ']';
        } else {
            result[j++] = address[i];
        }
    }
    result[j] = '\0';
    return result;
}