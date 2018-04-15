let local_host = 'http://0.0.0.0:8001'
//获取商品列表
export const getGoods = params => {
  return axios.get(`${local_host}/goods/`, {params: params})
}


//获取商品类别信息
export const getCategory = params => {
  if('id' in params){
    return axios.get(`${local_host}/categorys/`+params.id+'/');
  }
  else {
    return axios.get(`${local_host}/categorys/`, params);
  }
};
