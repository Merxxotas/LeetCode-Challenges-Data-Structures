class Solution {
	public boolean containsDuplicate(int[] nums){
		HashMap<Integer, Short> counter = new HashMap();
		for(int num : nums){
			if(counter.containsKey(num))
				return true;
			counter.put(num, (short)1);
		}
		return false;
	}
}
