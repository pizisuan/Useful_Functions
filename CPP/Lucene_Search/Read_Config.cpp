// 去除字符串两边空格
void strip(string& s)
{
	string::size_type i, j;
	for (i = 0; i < s.size() && isblank(s[i]); ++i);
	for (j = s.size(); j > 0 && isblank(s[j - 1]); --j);
	s = s.substr(i, j - i);
}

// 根据指定字符分割字符串(读取配置文件)    "port = 23333" 按‘=’分割为两部分 "port","23333"
pair<string, string> cut(const string& src_str, const char& letter)
{
	string::size_type pos = src_str.find(letter);
	string key = src_str.substr(0, pos);
	strip(key);
	string value = src_str.substr(pos + 1, src_str.size() - pos - 1);
	strip(value);
	return make_pair(key, value);
}

// 读取配置文件并获取其中的键值对
map<string, string> read_config (string file, bool ignore_empty = true) 
{
	map<string, string> cmap;
	cmap.clear();
	ifstream in(file.c_str());
	if (!in.good()) 
		return cmap;
	string line;
	while (getline(in, line)) 
	{
		strip(line);
		if (line.empty() || line[0] == '#') continue;
		vector<string> kp;
		size_t pos = line.find('=');
		if (pos == string::npos) 
			continue;
		string key = line.substr(0, pos);
		string value = line.substr(pos + 1, line.size() - pos - 1);
		strip(key);
		strip(value);
		if (ignore_empty && value.empty()) 
			continue;
		cmap[key] = value;
	}
	return cmap;
}
