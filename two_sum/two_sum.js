function two_sum_values(arr,target){
    const current_set = new Set()
    for (let i=0; i<arr.length;i++){
        let difference = target-arr[i]
        if(current_set.has(difference)){
            return [difference,arr[i]]
        }
        else{
            current_set.add(arr[i])
        }
    }
    return "No two values can sum up to target"
}

let [x,y] =two_sum_values([4,6,6,4,3,5,3,2],6)

console.log(x,y)